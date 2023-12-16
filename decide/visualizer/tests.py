import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.tests import BaseTestCase
from voting.models import Voting, Question, QuestionOption

class GraphicsViewTests(BaseTestCase):
    def setUp(self):
        q = Question(desc='Pregunta')
        q.save()
        opt1 = QuestionOption(question=q, option='Opcion 1')
        opt1.save()
        opt2 = QuestionOption(question=q, option='Opcion 2')
        opt2.save()

        voting_data = {
            "id": 1,
            "name": 'Votacion',
            "start_date": "2023-01-01",
            "end_date": "2023-01-01",
            "postproc": [
                {"option": "Opcion 1", "postproc": 10, "votes": 50},
                {"option": "Opcion 2", "postproc": 8, "votes": 40},
            ]
        }

        self.v = Voting(name='Votacion', question=q, postproc=voting_data)
        self.v.save()
        super().setUp()
    
    def tearDown(self):
        super().tearDown()
        self.v = None
    
    def testVotingExists(self):
        v = Voting.objects.get(name='Votacion')
        self.assertEquals(v.question.options.all()[0].option, "Opcion 1")
        self.assertEquals(v.postproc['postproc'][0]['votes'], 50)

    def testGraphicsViewWithValidId(self):
        v = Voting.objects.get(name='Votacion')
        voting_id = v.id
        url = reverse('graphics', args=[voting_id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'graphics/graphics.html')

    def testGraphicsViewWithInvalidId(self):
        voting_id = 999
        url = reverse('graphics', args=[voting_id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

class SeleniumGraphics(StaticLiveServerTestCase):
    def setUp(self):
        self.base = BaseTestCase()
        self.base.setUp()
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        
        q = Question(desc='Pregunta')
        q.save()
        opt1 = QuestionOption(question=q, option='Opcion 1')
        opt1.save()
        opt2 = QuestionOption(question=q, option='Opcion 2')
        opt2.save()
        opt3 = QuestionOption(question=q, option='Opcion 3')
        opt3.save()

        self.v = Voting(name='Votacion', question=q)
        self.v.save()
        self.v.create_pubkey()
        self.v.save()

        super().setUp()
    
    def tearDown(self):
        super().tearDown()
        self.driver.quit()
        self.base.tearDown()

    def testGetWinnerThereIsWin(self):
        v = Voting.objects.get(name='Votacion')
        v.postproc = [
            {"option": "Opcion 1", "votes": 50}, 
            {"option": "Opcion 2", "votes": 40},
            {"option": "Opcion 3", "votes": 30}
            ]
        v.save()

        self.driver.get('{}/visualizer/{}/graphics'.format(self.live_server_url, v.pk))
        time.sleep(1)
        winner_result = self.driver.find_element(By.ID, 'winnerResult').text
        total_votes_result = self.driver.find_element(By.ID, 'totalVotesResult').text

        self.assertEqual(winner_result, 'Opción ganadora de la votación: {}'.format(
            v.postproc[0]["option"]
        ))
        self.assertEqual(total_votes_result, 'Total de votos: {}'.format(
            120
        ))
    
    def testGetWinnerThereIsTie(self):
        v = Voting.objects.get(name='Votacion')
        v.postproc = [
            {"option": "Opcion 1", "votes": 50}, 
            {"option": "Opcion 2", "votes": 50},
            {"option": "Opcion 3", "votes": 50}
            ]
        v.save()

        self.driver.get('{}/visualizer/{}/graphics'.format(self.live_server_url, v.pk))
        time.sleep(1)
        winner_result = self.driver.find_element(By.ID, 'winnerResult').text
        total_votes_result = self.driver.find_element(By.ID, 'totalVotesResult').text

        self.assertEqual(winner_result, 'Empate entre {}, {}, {}'.format(
            v.postproc[0]["option"], v.postproc[1]["option"], v.postproc[2]["option"]
        ))
        self.assertEqual(total_votes_result, 'Total de votos: {}'.format(
            150
        ))
    
    def testGetWinnerThereIsNone(self):
        v = Voting.objects.get(name='Votacion')
        v.postproc = [
            {"option": "Opcion 1", "votes": 0}, 
            {"option": "Opcion 2", "votes": 0},
            {"option": "Opcion 3", "votes": 0}
            ]
        v.save()

        self.driver.get('{}/visualizer/{}/graphics'.format(self.live_server_url, v.pk))
        time.sleep(1)
        winner_result = self.driver.find_element(By.ID, 'winnerResult').text
        total_votes_result = self.driver.find_element(By.ID, 'totalVotesResult').text

        self.assertEqual(winner_result, 'No hay registros de votos')
        self.assertEqual(total_votes_result, 'Total de votos: {}'.format(
            0
        ))





        
