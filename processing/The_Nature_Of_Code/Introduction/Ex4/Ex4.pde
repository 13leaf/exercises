//Consider a simulation of paint splatter drawn as a collection of colored dots. Most of the paint clusters around a central location, but some dots do splatter out towards the edges. Can you use a normal distribution of random numbers to generate the locations of the dots? Can you also use a normal distribution of random numbers to generate a color palette?

Dot d;
void setup()
{
    size(600,600);
    d=new Dot();
    background(255);
}

void draw()
{
  d.step();
  d.render();
}
