package com.cdac;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class JdbcManagement 
{

	public void SelectById() throws ClassNotFoundException, SQLException 
	{
	
		//loading driver
		
		Class.forName("com.mysql.cj.jdbc.Driver");
		
		// get connection
		
	    Connection con=	DriverManager.getConnection("jdbc:mysql://localhost:3306/pgcpac","root","cdacacts");
		  //create query
		  
	      String q ="select  * from student where id = ?";
	      
	      //insert into student values(? ? ? )
	      
	    //create statement
		  	  	    
		  PreparedStatement   pmt=  con.prepareStatement(q);
		  	  
		  Scanner s = new Scanner(System.in);
		  System.out.println("enter the student id");
		  int n = s.nextInt();
		  
		  pmt.setInt(1, n);
		  
		  
		  ResultSet rs =pmt.executeQuery();
		  		  
	      //iterate the result
	      
	      while(rs.next())
	      {
	    	  
	    	  int id=rs.getInt(1);
	    	  String name = rs.getString(2);
	    	  int mark = rs.getInt(3);
	    	  System.out.println(id+name+mark);
	    	  
	      }
		
		
	}

	public void insertStudent() throws ClassNotFoundException, SQLException
	{
		
		
		  
		  Class.forName("com.mysql.cj.jdbc.Driver");
			
			// get connection
			
		    Connection con=	DriverManager.getConnection("jdbc:mysql://localhost:3306/pgcpac","root","cdacacts");
			  //create query
			  
		    Scanner s = new Scanner(System.in);
			  System.out.println("enter the student id,name,mark");
			  int n = s.nextInt();
			  String na = s.next();
			  int m = s.nextInt();
		    
		    
		      String q ="insert into student values(?,?,?)";
		      
		      PreparedStatement   pmt=  con.prepareStatement(q);
		      
		      pmt.setInt(1, n);
		      pmt.setString(2,na);
		      pmt.setInt(3, m);
		      
		     int row =pmt.executeUpdate();
		     System.out.println(row+ " "+ "record inserted");
		
		
		
		
		
		
		
		
	}

	public void deleteStudent() throws ClassNotFoundException, SQLException 
	{
		
		Scanner s = new Scanner(System.in);
		  System.out.println("enter the student id");
		  int n = s.nextInt();
		 
		  Class.forName("com.mysql.cj.jdbc.Driver");
			
			// get connection
			
		    Connection con=	DriverManager.getConnection("jdbc:mysql://localhost:3306/pgcpac","root","cdacacts");
			  //create query
			  
		      String q ="delete from student  where id = ?";
		      PreparedStatement   pmt=  con.prepareStatement(q);
		      	      
		      pmt.setInt(1, n);
		      
		     int row =pmt.executeUpdate();
		     System.out.println(row+ " "+ "record deleted");
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	}

	public void updateStudent() throws ClassNotFoundException, SQLException 
	{
		  Scanner s = new Scanner(System.in);
		  System.out.println("enter the student id,mark");
		  int n = s.nextInt();
		  int m = s.nextInt();
		  
		  Class.forName("com.mysql.cj.jdbc.Driver");
			
			// get connection
			
		    Connection con=	DriverManager.getConnection("jdbc:mysql://localhost:3306/pgcpac","root","cdacacts");
			  //create query
			  
		      String q ="update student set mark = ? where id = ?";
		      PreparedStatement   pmt=  con.prepareStatement(q);
		      
		      pmt.setInt(1, m);
		      pmt.setInt(2, n);
		      
		     int row =pmt.executeUpdate();
		     System.out.println(row+ " "+ "record updated");
		
	}

	
	
	
}
