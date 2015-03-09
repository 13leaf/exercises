// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com
//EX: In the above random walker, the result of the noise function is mapped directly to the Walker’s location. Create a random walker where you instead map the result of the noise() function to a Walker’s step size.

Walker w;
void setup() {
  size(500,500);
  // Create a walker object
  w = new Walker();
  background(255);
}

void draw() {
  // Run the walker object
  w.step();
  w.render();
}


