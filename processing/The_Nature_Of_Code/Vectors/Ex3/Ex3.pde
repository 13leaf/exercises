//TODO Extend the bouncing ball with vectors example into 3D. Can you get a sphere to bounce around a box?

void setup()
{
  size(640,360,P3D);
  background(0);
  noStroke();
  lights();
  
  pushMatrix();
  translate(width/2,height/2,0);
  rotateX(-PI/6);
  rotateY(-PI/3);
  box(120);
  popMatrix();
  
  pushMatrix();
  translate(160,160);
  sphere(50);
  popMatrix();
  
}

/**
//[full] Instead of a bunch of floats, we now just have two PVector variables.
PVector location; //[bold]
PVector velocity; //[bold]
//[end]

void setup() {
  size(640,360);
  location = new PVector(100,100); //[bold]
  velocity = new PVector(2.5,5); //[bold]
}

void draw() {
  background(255);

  location.add(velocity); //[bold]
  //[full] We still sometimes need to refer to the individual components of a PVector and can do so using the dot syntax: location.x, velocity.y, etc.
  if ((location.x > width) || (location.x < 0)) { //[bold]
    velocity.x = velocity.x * -1; //[bold]
  } //[bold]
  if ((location.y > height) || (location.y < 0)) { //[bold]
    velocity.y = velocity.y * -1; //[bold]
  } //[bold]
  //[end]

  stroke(0);
  fill(175);
  ellipse(location.x,location.y,16,16); //[bold]
}
*/
