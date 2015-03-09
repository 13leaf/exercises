// Daniel Shiffman
// The Nature of Code
// http://natureofcode.com
//Play with color, noiseDetail(), and the rate at which xoff and yoff are incremented to achieve different visual effects.

float increment = 0.02;

void setup() {
  size(800, 200);
  //noLoop();
}

void draw() {
  background(0);

  loadPixels();
  
    // Optional: adjust noise detail here
  float failOff=map(mouseX,0,width,0,1);
  println(failOff);
  noiseDetail(8,failOff);

  float xoff = 0.0; // Start xoff at 0

    // For every x,y coordinate in a 2D space, calculate a noise value and produce a brightness value
  for (int x = 0; x < width; x++) {
    xoff += increment;   // Increment xoff 
    float yoff = 0.0;   // For every xoff, start yoff at 0
    for (int y = 0; y < height; y++) {
      yoff += increment; // Increment yoff

      // Calculate noise and scale by 255
      float bright = noise(xoff, yoff)*255;

      // Try using this line instead
      //float bright = random(0,255);

      // Set each pixel onscreen to a grayscale value
      pixels[x+y*width] = color(bright);
    }
  }

  updatePixels();
}

