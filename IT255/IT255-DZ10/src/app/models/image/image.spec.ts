import { Image } from './image';

describe('Slike', () => {
  it('should create an instance', () => {
    expect(new Image(0, "", "", 0)).toBeTruthy();
  });
});
