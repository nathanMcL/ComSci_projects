package quizGame;

import java.awt.event.*;
import java.awt.*;
import javax.swing.*;


public class Quiz implements ActionListener
{
	String[] questions = {
							"What is a constructor in Java?",
							"How many Variables types are there in Java?",
							"How many Primitive data types are there?",
							"How do you call a method in Java?",
							"What is a common Access Modifier?"
						 };
	
	String[][] options = {
							{"a special method that is used to initialize objects", "a job title", "A setup method()","Frame work attributes"},
							{"3", "9", "5","6"},
							{"10", "8", "5", "9"},
							{";", "()", "[]", "++"},
							{"main", "void", "class", "public"}
						 };
	
	char[] answers =     {
							'A',
							'C',
							'B',
							'B',
							'D'
			
	                     };
	char guess;
	char answer;
	int index;
	int correct_guesses = 0;
	int total_questions = questions.length;
	int result;
	int seconds = 10;
	
	
	JFrame frame = new JFrame();
	Image backgroundImage; //background image
	JTextField textfield = new JTextField();
	JTextArea textarea = new JTextArea();
	JButton buttonA = new JButton();
	JButton buttonB = new JButton();
	JButton buttonC = new JButton();
	JButton buttonD = new JButton();
	JLabel answer_labelA = new JLabel();
	JLabel answer_labelB = new JLabel();
	JLabel answer_labelC = new JLabel();
	JLabel answer_labelD = new JLabel();
	JLabel time_label = new JLabel();
	JLabel seconds_left = new JLabel();
	JTextField number_right = new JTextField();
	JTextField percentage = new JTextField();
	//timer to count down each second for each question
	Timer timer = new Timer(1000, new ActionListener() {
		
		@Override
		public void actionPerformed(ActionEvent e) {
			seconds--;
			seconds_left.setText(String.valueOf(seconds));
			if(seconds<=0) {
				displayAnswer();
		}
			
		}
	});
//set the frame parameters
	public Quiz()
	{
		frame.setTitle("Java Quiz"); //frame title
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(700,700);
		frame.getContentPane().setBackground(new Color(0, 77, 26));
		frame.setLayout(null);
		frame.setResizable(false);
		//change the frame icon logo
		ImageIcon image = new ImageIcon("NM_logo.png");
		backgroundImage = new ImageIcon("linedNotePaper.png").getImage();//background image
		frame.setIconImage(image.getImage());
		
		
		textfield.setBounds(0,0,700,50);
		textfield.setBackground(new Color(0, 77, 26));//question # color
		textfield.setForeground(new Color(153,153,0));//question text color
		textfield.setFont(new Font("Cascadia Code",Font.BOLD,25));
		textfield.setBorder(BorderFactory.createBevelBorder(1));
		textfield.setHorizontalAlignment(JTextField.CENTER);
		textfield.setEditable(false);
		
		textarea.setBounds(0,50,700,50);
		textarea.setLineWrap(true);
		textarea.setWrapStyleWord(true);
		textarea.setBackground(new Color(153,153,0));//actual question color
		textarea.setForeground(new Color(0, 26, 17));//actual question text color
		textarea.setFont(new Font("Cascadia Code",Font.BOLD,20));
		textarea.setBorder(BorderFactory.createBevelBorder(1));
		textarea.setEditable(false);
		
		
		//Buttons
		buttonA.setBounds(0,100,100,100);
		buttonA.setFont(new Font("Cascadia Code",Font.BOLD,30));
		buttonA.setFocusable(false);
		buttonA.addActionListener(this);
		buttonA.setText("A");
		
		buttonB.setBounds(0,200,100,100);
		buttonB.setFont(new Font("Cascadia Code",Font.BOLD,30));
		buttonB.setFocusable(false);
		buttonB.addActionListener(this);
		buttonB.setText("B");
		
		buttonC.setBounds(0,300,100,100);
		buttonC.setFont(new Font("Cascadia Code",Font.BOLD,30));
		buttonC.setFocusable(false);
		buttonC.addActionListener(this);
		buttonC.setText("C");
		
		buttonD.setBounds(0,400,100,100);
		buttonD.setFont(new Font("Cascadia Code",Font.BOLD,30));
		buttonD.setFocusable(false);
		buttonD.addActionListener(this);
		buttonD.setText("D");
		
		answer_labelA.setBounds(125,100,500,100);
		answer_labelA.setBackground(new Color(50,50,50));
		answer_labelA.setForeground(new Color(25,255,0));
		answer_labelA.setFont(new Font("Cascadia Code",Font.PLAIN,16));
				
		answer_labelB.setBounds(125,200,500,100);
		answer_labelB.setBackground(new Color(50,50,50));
		answer_labelB.setForeground(new Color(25,255,0));
		answer_labelB.setFont(new Font("Cascadia Code",Font.PLAIN,25));
				
		answer_labelC.setBounds(125,300,500,100);
		answer_labelC.setBackground(new Color(50,50,50));
		answer_labelC.setForeground(new Color(25,255,0));
		answer_labelC.setFont(new Font("Cascadia Code",Font.PLAIN,25));
				
		answer_labelD.setBounds(125,400,500,100);
		answer_labelD.setBackground(new Color(50,50,50));
		answer_labelD.setForeground(new Color(25,255,0));
		answer_labelD.setFont(new Font("Cascadia Code",Font.PLAIN,25));
				
		seconds_left.setBounds(535,510,100,100);
		seconds_left.setBackground(new Color(25,25,25));
		seconds_left.setForeground(new Color(255,0,0));
		seconds_left.setFont(new Font("Stencil",Font.PLAIN,50));
		seconds_left.setBorder(BorderFactory.createBevelBorder(1));
		seconds_left.setOpaque(true);
		seconds_left.setHorizontalAlignment(JTextField.CENTER);
		seconds_left.setText(String.valueOf(seconds));
		
		time_label.setBounds(535,475,100,25);
		time_label.setBackground(new Color(0, 77, 26));
		time_label.setForeground(new Color(255,0,0));
		time_label.setFont(new Font("Cascadia Code",Font.PLAIN,20));
		time_label.setHorizontalAlignment(JTextField.CENTER);
		time_label.setText("timer");
		//displays number correct at the end 
		number_right.setBounds(225,225,200,100);
		number_right.setBackground(new Color(25,25,25));
		number_right.setForeground(new Color(25,255,0));
		number_right.setFont(new Font("Cascadia Code",Font.PLAIN,40));
		number_right.setBorder(BorderFactory.createBevelBorder(1));
		number_right.setHorizontalAlignment(JTextField.CENTER);
		number_right.setEditable(false);
		
		percentage.setBounds(225,325,200,100);
		percentage.setBackground(new Color(25,25,25));
		percentage.setForeground(new Color(25,255,0));
		percentage.setFont(new Font("Cascadia Code",Font.PLAIN,40));
		percentage.setBorder(BorderFactory.createBevelBorder(1));
		percentage.setHorizontalAlignment(JTextField.CENTER);
		percentage.setEditable(false);
		
		
		frame.add(time_label);
		frame.add(seconds_left);
		frame.add(answer_labelA);
		frame.add(answer_labelB);
		frame.add(answer_labelC);
		frame.add(answer_labelD);
		frame.add(buttonA);
		frame.add(buttonB);
		frame.add(buttonC);
		frame.add(buttonD);
		frame.add(textarea);
		frame.add(textfield);
		frame.setVisible(true);
		
		nwxtQuestion();
	}
	//-----------------------
	public void nwxtQuestion() 
	{
			if(index>=total_questions)
			{
				results();
			}
			else 
			{
				textfield.setText("Question " + (index+1));
				textarea.setText(questions[index]);
				answer_labelA.setText(options[index][0]);
				answer_labelB.setText(options[index][1]);
				answer_labelC.setText(options[index][2]);
				answer_labelD.setText(options[index][3]);
				timer.start();
			}
	}
	//-----------------------
	@Override
	public void actionPerformed(ActionEvent e) 
	{
			buttonA.setEnabled(false);
			buttonB.setEnabled(false);
			buttonC.setEnabled(false);
			buttonD.setEnabled(false);
			
			if(e.getSource()==buttonA) {
				answer = 'A';
				if(answer == answers[index]) {
					correct_guesses++;
				}
			}
			if(e.getSource()==buttonB) {
				answer = 'B';
				if(answer == answers[index]) {
					correct_guesses++;
				}
			}
			if(e.getSource()==buttonC) {
				answer = 'C';
				if(answer == answers[index]) {
					correct_guesses++;
				}
			}
			if(e.getSource()==buttonD) {
				answer = 'D';
				if(answer == answers[index]) {
					correct_guesses++;
				}
			}
			displayAnswer();
	}
	//-----------------------
	public void displayAnswer()
	{
		timer.stop();
		buttonA.setEnabled(false);
		buttonB.setEnabled(false);
		buttonC.setEnabled(false);
		buttonD.setEnabled(false);
		
		if(answers[index] != 'A')
			answer_labelA.setForeground(new Color(255,0,0));
		if(answers[index] != 'B')
			answer_labelB.setForeground(new Color(255,0,0));
		if(answers[index] != 'C')
			answer_labelC.setForeground(new Color(255,0,0));
		if(answers[index] != 'D')
			answer_labelD.setForeground(new Color(255,0,0));
		
		//timer is set prior to the start of each new set of question
		Timer pause = new Timer(3000, new ActionListener() 
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				answer_labelA.setForeground(new Color(25,255,0));
				answer_labelB.setForeground(new Color(25,255,0));
				answer_labelC.setForeground(new Color(25,255,0));
				answer_labelD.setForeground(new Color(25,255,0));
				
				answer = ' ';
				seconds=10;
				seconds_left.setText(String.valueOf(seconds));
				buttonA.setEnabled(true);
				buttonB.setEnabled(true);
				buttonC.setEnabled(true);
				buttonD.setEnabled(true);
				index++;
				nwxtQuestion();
			}
		});
		pause.setRepeats(false);
		pause.start();
		
	}
	//-----------------------
	public void results() 
	{
		buttonA.setEnabled(false);
		buttonB.setEnabled(false);
		buttonC.setEnabled(false);
		buttonD.setEnabled(false);
		
		result = (int)((correct_guesses/(double)total_questions)*100);
		
		textfield.setText("RESULTS!");
		textarea.setText("");
		answer_labelA.setText("");
		answer_labelB.setText("");
		answer_labelC.setText("");
		answer_labelD.setText("");
		
		number_right.setText("("+correct_guesses+"/"+total_questions+")");
		percentage.setText(result+"%");
		
		
		frame.add(percentage);
		frame.add(number_right);
	}
	
}
