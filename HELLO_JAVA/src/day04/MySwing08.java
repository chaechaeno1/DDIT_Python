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

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 325, 453);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫 별 수 : ");
		lbl_first.setBounds(55, 39, 57, 15);
		contentPane.add(lbl_first);
		
		JLabel lbl_last = new JLabel("끝 별 수 : ");
		lbl_last.setBounds(55, 84, 57, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(124, 36, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(124, 81, 116, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(55, 120, 185, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(31, 156, 249, 224);
		contentPane.add(ta);
	}
	
	String getStar(int cnt) {
		String txt = "";
		for(int i = 0; i<= cnt;i++) {
			txt+="*";
		}
		return txt;
	}
	
	void myClick() {
	    String star1 = tf_first.getText();
	    String star2 = tf_last.getText();

	    int istar1 = Integer.parseInt(star1);
	    int istar2 = Integer.parseInt(star2);

	    String star = "";
	    for (int i = istar1; i <= istar2; i++) { 
	        star += getStar(i) + "\n";
	    }
	    ta.setText(star);
	}
		

	}


