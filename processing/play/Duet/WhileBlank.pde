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
