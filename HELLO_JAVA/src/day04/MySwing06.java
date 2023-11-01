package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 262, 416);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력 단수");
		lbl.setBounds(58, 42, 106, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(132, 39, 59, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
				
			}
		});
		btn.setBounds(46, 67, 145, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(46, 109, 145, 214);
		contentPane.add(ta);
	}
	
	void myClick() {
		String dan = tf.getText(); //직접 입력한 수를 String dan으로 선언
		int idan = Integer.parseInt(dan); //문자열 dan을 정수형으로 변환
		
		String code = ""; //반복문 담을 변수 선언
		int res = 0; //결과값 담을 변수 선언
		for(int i = 1; i<10 ;i++) {			
			res = idan*i; //idan은 직접 입력한 단수	
			code += dan +" * " + i + " = " + res +"\n";			
			ta.setText(code);
		}
		
		

				
			
	}
	
}
