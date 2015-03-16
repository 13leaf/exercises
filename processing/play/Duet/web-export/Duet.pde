float angle=0;
float step=3;
int direction=1;
boolean userControl=false;
int radius = 80;
float childRadius=15;
int fixedWidth=radius*3+radius/2;
WhiteBlankFactory factory=new WhiteBlankFactory();

ArrayList<WhiteBlank> blanks=new ArrayList<WhiteBlank>();

void setup()
{
  size(600, 800);
  frameRate(120);
  blanks.add(factory.newLeftFlat(-600));
  blanks.add(factory.newLeftFlat(-400));
  blanks.add(factory.newLeftFlat(-200));
  blanks.add(factory.newRightFlat(200));
  //blanks.add(factory.newLeftRect(200));
//  blanks.add(factory.newRightRect(400));
  //noLoop();
}

void keyPressed()
{
  if(keyCode == LEFT || key == 'a'){
      direction=-1;
      userControl=true;
  }else if(keyCode == RIGHT || key == 'd'){
      direction=1;
      userControl=true;
  }
}

void keyReleased()
{
  userControl=false;
}

void mousePressed()
{
  if(mouseX<width/2){
    direction=-1;
    userControl=true;
  }else{
    direction=1;
    userControl=true;  
  }
}

void mouseReleased()
{
  userControl=false;
}

void draw()
{
  background(0);

  for(int i=0;i<blanks.size();i++){
    blanks.get(i).step();
    blanks.get(i).display();
  }

  pushMatrix();
  stroke(250, 100);
  translate(width/2, height-radius-40);
  if(userControl){
    angle=(angle+step*direction)%360;  
  }
  rotate(radians(angle));
  noFill();
  ellipse(0, 0, radius*2, radius*2);

  noStroke();
  fill(0, 0, 255);
  ellipse(-radius, 0, childRadius*2, childRadius*2);
  fill(255, 0, 0);
  ellipse(radius, 0, childRadius*2, childRadius*2);

  popMatrix();

}

class WhiteBlankFactory
{
  public WhiteBlank newLeftFlat(int y)
  {
    return new WhiteBlank(0,y,radius*2,30);
  }
  
  public WhiteBlank newRightFlat(int y)
  {
     return new WhiteBlank(fixedWidth-radius*2,y,radius*2,30);
  }
  
  public WhiteBlank newLeftRect(int y)
  {
    return new WhiteBlank((int)(fixedWidth/2-radius-childRadius),y,100,100);
  }
  
  public WhiteBlank newRightRect(int y)
  {
    return new WhiteBlank((int)(radius*2+childRadius-50),y,100,100);
  }
}

class WhiteBlank
{
   int x;
   int y;
   int w;
   int h;
   
   public WhiteBlank(int x,int y,int w,int h)
   {
     this.x=x;
     this.y=y;
     this.w=w;
     this.h=h;
   }
   
   public void step()
   {
       y+=3;
       if(y>height) y=0;
   }
   
   public void display()
   {
     pushMatrix();
     noStroke();
     fill(255);
     translate(map(x,0,fixedWidth,width/2-fixedWidth/2,width/2+fixedWidth/2),y);
     rect(0,0,w,h);
     popMatrix();
   }
}

