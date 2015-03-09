// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com
//EX: Create a random walker with dynamic probabilities. For example, can you give it a 50% chance of moving in the direction of the mouse?

Walker w;

void setup() {
  size(800,200);
  // Create a walker object
  w = new Walker();
  background(255);
}

void draw() {
  // Run the walker object
  w.step();
  w.render();
}


