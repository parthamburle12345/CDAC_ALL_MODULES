package com.cdac;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JdbcStatementExample 
{

	public static void main(String[] args) throws SQLException, ClassNotFoundException 
	{
	
		//loading driver
		
		Class.forName("com.mysql.cj.jdbc.Driver");
		
		// get connection
		
	 Connection con=	DriverManager.getConnection("jdbc:mysql://localhost:3306/pgcpac","root","cdacacts");
		
	  //create statement
	  
	  Statement   smt=  con.createStatement();
		                     
	  	//create query
	  
	      String q ="select  * from student";
	  	
	      ResultSet rs= smt.executeQuery(q);
	      
	      //iterate the result
	      
	      while(rs.next())
	      {
	    	  
	    	  int id=rs.getInt(1);
	    	  String name = rs.getString(2);
	    	  int mark = rs.getInt(3);
	    	  System.out.println(id+name+mark);
	    	  
	      }
	      
		
		
	}
}
