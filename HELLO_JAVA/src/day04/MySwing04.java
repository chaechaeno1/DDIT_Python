package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MySwing04 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl1 = new JLabel("__");
		lbl1.setBounds(46, 42, 57, 15);
		contentPane.add(lbl1);
		
		JLabel lbl2 = new JLabel("__");
		lbl2.setBounds(100, 42, 57, 15);
		contentPane.add(lbl2);
		
		JLabel lbl3 = new JLabel("__");
		lbl3.setBounds(181, 42, 57, 15);
		contentPane.add(lbl3);
		
		JLabel lbl4 = new JLabel("__");
		lbl4.setBounds(269, 42, 57, 15);
		contentPane.add(lbl4);
		
		JLabel lbl5 = new JLabel("__");
		lbl5.setBounds(325, 42, 57, 15);
		contentPane.add(lbl5);
		
		JLabel lbl6 = new JLabel("__");
		lbl6.setBounds(377, 42, 57, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
			int[] num = new int[6];
			Random rnd = new Random();
			
			for(int i=0; i<6;i++) {
				num[i]=rnd.nextInt(45)+1; 
				// 0~45까지 범위의 난수 발생
				//45 -> 0~44까지만 나옴				
			}
				lbl1.setText(num[0]+"");
				lbl2.setText(num[1]+"");
				lbl3.setText(num[2]+"");
				lbl4.setText(num[3]+"");
				lbl5.setText(num[4]+"");
				lbl6.setText(num[5]+"");
	
			}
		});
		btn.setBounds(67, 88, 313, 23);
		contentPane.add(btn);
	}
	
}
