/* 
 * The dictionary is using the english Open Word LIst:http://dreamsteep.com/downloads/word-games-and-wordsmith-utilities/120-the-english-open-word-list-eowl.html
 * 
 * 
 * 
 */
package com.bigdata;
import java.io.*;


import java.util.ArrayList;
public class lexAnalysis {
	
	private final String DicFilePath;
	private ArrayList<String > Dic=new ArrayList<String>();

	//constructor with dictionary path
	lexAnalysis(final String path) throws IOException	
	{
		this.DicFilePath=path;
		this.ReadDic();
	}
	

    
	private void ReadDic() throws IOException
	{
		BufferedReader reader=new BufferedReader(new FileReader(this.DicFilePath));
		String StdWord=null;
		while((StdWord=reader.readLine()) != null)
		{			
			this.Dic.add(StdWord);
		}
		
	
	}
		
		
	public boolean SpellCheck(String word) throws IOException
	{		
	for(String str :this.Dic)				
	{
		if(str.equals(word)){
			return true;
		}
	}
		
	return false;	
	}
	
	
}
	
	


