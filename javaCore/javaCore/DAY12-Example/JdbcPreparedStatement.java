package com.cdac;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class JdbcPreparedStatement 
{
public static void main(String[] args) throws ClassNotFoundException, SQLException 
{

	JdbcManagement jm = new JdbcManagement();
	
			
			jm.SelectById();
		//	jm.insertStudent();
		//jm.updateStudent();
		//	jm.deleteStudent();	
			
} 

}
