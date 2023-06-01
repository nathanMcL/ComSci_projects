
import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class GameFrame extends JFrame {
	
	GameFrame() {
		
		this.add(new GamePanel());
		this.setTitle("Snake");
		//change the frame icon logo
		//ImageIcon image = new ImageIcon("NM_logo.png");
		//this.setIconImage(image.getImage());
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setResizable(false);
		this.pack();
		this.setVisible(true);
		this.setLocationRelativeTo(null);
	}

}
