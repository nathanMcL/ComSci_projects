package balls;


import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.BorderFactory;

//This program bounces two balls around a sizable grey screen. 
//The balls change color each time a ball touches a side.
//If the balls collide a message is generated to the console.
//The user can change the direction of travel through the mouse buttons
//***After the balls collide the background should change.
//***When the balls collide a new ball is generated
//***A bouncing sound effect should play
public class BouncingBalls extends JPanel implements ActionListener {

	private static final int DELAY = 10; //speed milliseconds: variable specifies the number of milliseconds between each repaint event.
    private int x1 = 100;// variables specify the initial position and velocity of the first ball.
    private int y1 = 400;
    private int dx1 = 5;
    private int dy1 = 5;
    private Color color1 = Color.blue;

    private int x2 = 300;//variables specify the initial position and velocity of the second ball.
    private int y2 = 100;
    private int dx2 = 5;
    private int dy2 = 5;
    private Color color2 = Color.red;
    
 public static void main(String[] args) {
	 
	 	SoundEffect SF = new SoundEffect();
    	
    	Border border = BorderFactory.createLineBorder(Color.GREEN,4);
    	
    	JFrame frame = new JFrame("Bouncing Balls");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new BouncingBalls());
        frame.setSize(500, 500);
        //frame.setBorder(border);
        
        ImageIcon image = new ImageIcon("NM_logo.png");
        frame.setIconImage(image.getImage());
        frame.setResizable(true);
        frame.setVisible(true);
    }
 
//mouse option to change direction of ball travel
    public BouncingBalls() {
        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                dx1 = -dx1;
                dy1 = -dy1;
                dx2 = -dx2;
                dy2 = -dy2;
            }
        });

        new Timer(DELAY, this).start();
    }

    public BouncingBalls(int newX, int newY, int newDx, int newDy, Color newColor) {
    	  x1 = newX;
          y1 = newY; 
          dx1 = newDx;
          dy1 = newDy;
          color1 = newColor;
      }
	

	@Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        g.setColor(Color.DARK_GRAY);
        g.fillRect(0, 0, getWidth(), getHeight());

        g.setColor(color1);
        g.fillOval(x1, y1, 80, 80);

        g.setColor(color2);
        g.fillOval(x2, y2, 50, 50);
    }
	//if a ball touches a side it will change colors
    @Override
    public void actionPerformed(ActionEvent e) {
        x1 += dx1;
        y1 += dy1;

        if (x1 < 0 || x1 > getWidth() - 50) {
            dx1 = -dx1;
            color1 = getRandomColor();
        }

        if (y1 < 0 || y1 > getHeight() - 50) {
            dy1 = -dy1;
            color1 = getRandomColor();
        }

        x2 += dx2;
        y2 += dy2;

        if (x2 < 0 || x2 > getWidth() - 50) {
            dx2 = -dx2;
            color2 = getRandomColor();
        }

        if (y2 < 0 || y2 > getHeight() - 50) {
            dy2 = -dy2;
            color2 = getRandomColor();
        }
        	//detects is the balls collide
        if (x1 + 50 >= x2 && x1 <= x2 + 50 && y1 + 50 >= y2 && y1 <= y2 + 50) { 
            System.out.println("collision detected");
            
            Container container = new Container();//change color of background if balls collide
			this.setBackground(Color.BLACK);// background not changing to black
			

            // Bounce the balls off each other
			int tempDx = dx1;
            int tempDy = dy1;
            dx1 = dx2;
            dy1 = dy2;
            dx2 = tempDx;
            dy2 = tempDy;
            
            
           
            
            //create a new ball each time a collision happens
            int newX = (int) (Math.random() * (getWidth() - 50)) + 25;
            int newY = (int) (Math.random() * (getWidth() - 50)) + 25;
            int newDx = (Math.random() > 0.5) ? 5: -5;
            int newDy = 5;
            Color newColor = getRandomColor();
            
            //add the new ball to the panel
            add(new BouncingBalls(newX, newY, newDx,newDy, newColor));
            
        } 
        
        repaint();
    }
    
    

    private Color getRandomColor() {
        int red = (int) (Math.random() * 255);
        int green = (int) (Math.random() * 255);
        int blue = (int) (Math.random() * 255);
        return new Color(red, green, blue);
    }

   
}





