// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com
//Find something you’ve previously made in Processing using separate x and y variables and use PVectors instead.
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



// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

// A random walker object!

class Walker {
  PVector loc;

  Walker() {
    loc=new PVector(width/2,height/2);
  }

  void render() {
    stroke(0);
    strokeWeight(2);
    point(loc.x,loc.y);
  }

  // Randomly move up, down, left, right, or stay in one place
 void step() {
    
    float r = random(1);
    //70% go right,30% go left
    if(r<0.7){
      loc.x++;
    }else{
      loc.x--;
    }
    //60% down,40%up
    if(r<0.6){
      loc.y++;
    }else{
      loc.y--;
    }
  
    loc.x = constrain(loc.x,0,width-1);
    loc.y = constrain(loc.y,0,height-1);
  }
}


