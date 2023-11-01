package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextField;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 268, 307);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나:");
		lblMine.setBounds(55, 50, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴:");
		lblCom.setBounds(55, 101, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과:");
		lblResult.setBounds(55, 156, 57, 15);
		contentPane.add(lblResult);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
				
			}
		});
		btn.setBounds(55, 197, 139, 23);
		contentPane.add(btn);
		
		tfMine = new JTextField();
		tfMine.setBounds(78, 47, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(78, 98, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(93, 153, 102, 21);
		contentPane.add(tfResult);
	}
	
	void myClick() {
		String mine = tfMine.getText();
		String com = "";
		String res = "";
		
		double rnd = (double) Math.random();
		if(rnd > 0.66) com = "가위";
		else if(rnd <0.33) com ="바위";
		else com = "보";
		
		if(mine.equals(com)) 
			res = "비김";
		else if( (mine=="가위" && com=="보") || (mine=="바위" && com=="가위") || (mine=="보" && com=="바위")) {
			res = "이김";
		}else {
			res = "짐..";
		}
		
		tfCom.setText(com);
		tfResult.setText(res);
		
	}

}
