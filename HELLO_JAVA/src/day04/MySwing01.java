package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing01 extends JFrame { //생성

	private JPanel pan;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing01 frame = new MySwing01();
					frame.setVisible(true); //비지블
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300); //사이즈
		pan = new JPanel(); //Panel이 하나 더 있는 것!
		pan.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(pan);
		pan.setLayout(null);
		
		JLabel lbl = new JLabel("Good Morning");
		lbl.setBounds(63, 172, 97, 15);
		pan.add(lbl);
		
		JButton btn = new JButton("CLICK !!");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				lbl.setText("Good Evening");
			}
		});

		btn.setBounds(169, 215, 97, 23);
		pan.add(btn);
		

	}
}
