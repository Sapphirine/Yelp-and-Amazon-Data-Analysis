/*
 * 
 * 
*@Author: Zhibo Wan 
*
*
*
*
*/

package com.bigdata;
//import java.util.Scanner;
import java.io.*;

import net.sf.javaml.clustering.KMeans;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;
import java.util.Map;


public class main {
	
	
	private static final String COMMA_DELIMITER=",";
	private static final String NEW_LINE_SEPARATOR = "\n";	
	
	
	/**
	 * @param args
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader reader=new BufferedReader(new FileReader("user.csv"));
		String line=null;
		FileWriter fileWriter=new FileWriter("output.csv");
		
        int TotalWordCount=0;
        HashMap<String,Integer> TotalMap=new HashMap<>();
        
        lexAnalysis lex=new lexAnalysis("./dic/all.csv");
        
        
		while((line=reader.readLine())!=null)
		  {
			
		
			String tmp=null;
		
			String ReviewerID;
			if(line.indexOf(',')>0)
			{ ReviewerID=line.substring(0,line.indexOf(','));}
			else
			{ReviewerID=null;}
			try{
			fileWriter.append(ReviewerID);
			fileWriter.append(COMMA_DELIMITER);
			}catch (Exception e){System.out.println("");e.printStackTrace();}
			
			
			
	
			tmp=line.substring(line.indexOf(',')+1,line.length());
			tmp=tmp.substring(tmp.indexOf(',')+1,tmp.length());
			tmp=tmp.substring(tmp.indexOf(',')+1,tmp.length());
			
			String[] words=tmp.split("\\W+");
			
			
			HashMap<String,Integer> WordMap=new HashMap<String,Integer>();
			
			int wordCount=0;
			int UsefulWord=0;
			for(String tmp1:words)
			{   
				if(tmp1.matches("[-+]?\\d*\\.?\\d+")||tmp1.length()<1)//if string is not alpehbia word ,skip
				{continue;}			
				
				tmp1=tmp1.toLowerCase();
				++wordCount;//for word count
				if(lex.SpellCheck(tmp1))
				{
				++UsefulWord;	
				}
				
				
				if(!WordMap.containsKey(tmp1))
				{
					WordMap.put(tmp1, 1);
					if(!TotalMap.containsKey(tmp1))
					{
						TotalMap.put(tmp1, 1);
					}
					
					else
					{TotalMap.put(tmp1,TotalMap.get(tmp1)+1);}
					
				
				}
				else
				{
					WordMap.put(tmp1, WordMap.get(tmp1)+1);
					TotalMap.put(tmp1,TotalMap.get(tmp1)+1);
				}
								
				//System.out.println(tmp1);
				
			}
             //get rid of last dates format
            
			Set set=WordMap.entrySet();
			Iterator iterator=set.iterator();
			
			while(iterator.hasNext()){
				
				
				
				Map.Entry mentry=(Map.Entry)iterator.next();
				fileWriter.append((CharSequence) mentry.getKey());
				fileWriter.append(COMMA_DELIMITER);
				
				//System.out.print(mentry.getKey()+"  ");
				fileWriter.append((CharSequence) String.valueOf(mentry.getValue()));
				fileWriter.append(COMMA_DELIMITER);
				
				

				
			}
			
			fileWriter.append("TOTAL,");
			fileWriter.append((CharSequence) String.valueOf(wordCount));
			fileWriter.append(COMMA_DELIMITER);
			fileWriter.append((CharSequence) String.valueOf(UsefulWord));
			fileWriter.append(NEW_LINE_SEPARATOR);
			
			
			TotalWordCount=TotalWordCount+wordCount;//increase total amount
			
			
			
			
			
		}//While
		
		
        //printout the result of total map
		Set set=TotalMap.entrySet();
		Iterator iterator=set.iterator();
		
		FileWriter fileWriter1=new FileWriter("WordOutput.csv");
		int NumOfDiffWord=0;
		while(iterator.hasNext()){						
			++NumOfDiffWord;
			
			Map.Entry mentry=(Map.Entry)iterator.next();
			fileWriter1.append((CharSequence) mentry.getKey());
			fileWriter1.append(COMMA_DELIMITER);
			System.out.print(mentry.getKey()+"  ");
			fileWriter1.append((CharSequence) String.valueOf(mentry.getValue()));
			System.out.println(mentry.getValue());
			fileWriter1.append(NEW_LINE_SEPARATOR);
			
			
		}
		
		
		
		//System.out.println("hello");
	reader.close();
	fileWriter.close();
	fileWriter1.close();
	System.out.println("Total WordCount is: "+TotalWordCount);
	System.out.println("Total Different WordCount is: "+NumOfDiffWord);
	System.out.println("Number of <the> is "+TotalMap.get("the"));
	
	
	
KMeans km=new KMeans(3);
	
	
	
	
	}

	
	
	
}
