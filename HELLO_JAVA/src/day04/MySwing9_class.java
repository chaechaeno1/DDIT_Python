package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JDialog;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing9_class extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing9_class frame = new MySwing9_class();
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
	public MySwing9_class() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 313, 316);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(JTextField.RIGHT); //우측정렬 추가
		tf.setBounds(35, 29, 219, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn1.setBounds(35, 60, 70, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn2.setBounds(110, 60, 70, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn3.setBounds(184, 60, 70, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn4.setBounds(35, 93, 70, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn5.setBounds(110, 93, 70, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn6.setBounds(184, 93, 70, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn7.setBounds(35, 126, 70, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn8.setBounds(110, 126, 70, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn9.setBounds(184, 126, 70, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
			
		});
		btn0.setBounds(35, 159, 70, 23);
		contentPane.add(btn0);
		
		
		
		JButton btn_call = new JButton("☎");
		btn_call.addMouseListener(new MouseAdapter() {

			
			@Override
			public void mouseClicked(MouseEvent e) {
				
				mycall();

			}
		});
		btn_call.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn_call.setBounds(110, 159, 144, 23);
		contentPane.add(btn_call);
	}
	
	
	void myclick(MouseEvent e) {
		JButton temp =  (JButton) e.getComponent();
		String str_new = temp.getText();
		
		String str_old = tf.getText();
		tf.setText(str_old+str_new);
		
	}
	void mycall() {
		String str_tel = tf.getText();
		JOptionPane.showMessageDialog(null, "Calling to\n"+str_tel);
		
	}
	

}
