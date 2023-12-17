import TransitionView from '@/components/View/TransitionView.vue';
import { mount } from '@vue/test-utils';

test('transition component should render correctly', () => {
  const wrapper = mount(TransitionView);

  expect(wrapper.findComponent({ name: 'transition' }).exists()).toBe(true);
});
