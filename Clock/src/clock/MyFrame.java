package clock;

import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.text.SimpleDateFormat;
import java.util.Calendar;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class MyFrame extends JFrame{
	
	
	Calendar calendar;
	SimpleDateFormat timeFormat;
	SimpleDateFormat dayFormat;
	SimpleDateFormat dateFormat;
	JLabel timeLabel;
	JLabel dayLabel;
	JLabel dateLabel;
	String time;
	String day;
	String date;
	
	MyFrame() {
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setTitle("The Time");
		this.setLayout(new FlowLayout());
		this.setSize(350,200);
		this.setResizable(false);
		//format can be changed. 
		timeFormat = new SimpleDateFormat("hh:mm:ss a");
		dayFormat = new SimpleDateFormat("EEEE");
		dateFormat = new SimpleDateFormat("MMMMM dd, yyyy");
		
		timeLabel = new JLabel();
		timeLabel.setFont(new Font("Cascadia Code",Font.PLAIN,50 ));
		timeLabel.setForeground(new Color(0x00FF00));
		timeLabel.setBackground(Color.BLACK);
		timeLabel.setOpaque(true);
		
		dayLabel = new JLabel();
		dayLabel.setFont(new Font("Cascadia Mono",Font.PLAIN,30 ));
		
		dateLabel = new JLabel();
		dateLabel.setFont(new Font("Cascadia Mono",Font.PLAIN,30 ));
				
		this.add(timeLabel);
		this.add(dayLabel);
		this.add(dateLabel);
		this.setVisible(true);
		
		//method to increment the clock every second
		setTime();
		
	}
	
	public void setTime() {
		while(true) {
		//current time	
		time = timeFormat.format(Calendar.getInstance().getTime());
		timeLabel.setText(time);
		//day of the week 
		day = dayFormat.format(Calendar.getInstance().getTime());
		dayLabel.setText(day);
		//current date
		date = dateFormat.format(Calendar.getInstance().getTime());
		dateLabel.setText(date);
		
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			}
		}
	}
	
		
}
