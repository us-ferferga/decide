from rest_framework.views import APIView
from rest_framework.response import Response

class PostProcView(APIView):

    def identity(self, options):
        out = []

        for opt in options:
            out.append({
                **opt,
                'postproc': opt['votes'],
            });

        out.sort(key=lambda x: -x['postproc'])
        return Response(out)
    
    def dhondt(self, options):
        nSeats = int(self.request.data.get('seats'))
        
        seats = {}
        results = {}
        
        for opt in options:
            option_name = opt['option']
            if option_name not in results:
                results[option_name] = opt['votes']
            else:
                results[option_name].append(opt['votes'])
        
        t_votes = results.copy()

        for key in results:
            seats[key] = 0

        for seat in range(nSeats):
            #Selecciona la opcion con el mayor cociente de votos
            next_seat = max(t_votes, key=t_votes.get)
            
            #Incrementa el numero de escaños
            if next_seat in seats:
                seats[next_seat] += 1
            else:
                seats[next_seat] = 1
            
            #Carga los votos temporales segun Dhondt
            t_votes[next_seat] = results[next_seat] / (seats[next_seat] + 1)

        return Response(seats)

    def post(self, request):
        """
         * type: IDENTITY | EQUALITY | WEIGHT
         * options: [
            {
             option: str,
             number: int,
             votes: int,
             ...extraparams
            }
           ]
        """

        t = request.data.get('type', 'IDENTITY')
        opts = request.data.get('options', [])

        if t == 'IDENTITY':
            return self.identity(opts)
        if t == 'DHONDT':
            return self.dhondt(opts)

        return Response({})
