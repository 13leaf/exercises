import java.util.*;

class Dot
{
  float x,y,stroke;
  Random r=new Random();

  Dot() {
  }
  
  void step()
  {
    stroke=constrain((float)r.nextGaussian()*70+100,0,255);
    x=constrain((float)r.nextGaussian()*100+width/2,0,width);
    y=constrain((float)r.nextGaussian()*100+height/2,0,height);
  }

  void render() {
    stroke(stroke);
    strokeWeight(4);
    point(x,y);
  }
}
