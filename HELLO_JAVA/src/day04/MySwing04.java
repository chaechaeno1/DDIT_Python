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
				
				
				int array[] = myClick();
				lbl1.setText(array[0]+"");
				lbl2.setText(array[1]+"");	
				lbl3.setText(array[2]+"");	
				lbl4.setText(array[3]+"");	
				lbl5.setText(array[4]+"");	
				lbl6.setText(array[5]+"");	
				
				
			}
		});
		btn.setBounds(67, 88, 313, 23);
		contentPane.add(btn);
	}
	
	int[] myClick(){
		
		int[] array = new int[45];

		for(int i =0; i <45; i++) {
			array[i] = i+1;
		}
		
		//랜덤 돌리는 횟수 = 1000번	
		for(int i=0; i<1000;i++) {

			int rnd= (int)(Math.random()*45);
	
			//랜덤 섞기
			int temp = array[i];
			array[i] = array[rnd];
			array[rnd] = temp;
			
		}
		return array;

		
		
	}

}
