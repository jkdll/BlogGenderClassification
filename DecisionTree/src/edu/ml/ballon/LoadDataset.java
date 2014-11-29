package edu.ml.ballon;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class LoadDataset {
	private ArrayList<String> colour=new ArrayList<String>();
	private ArrayList<String> size=new ArrayList<String>();
	private ArrayList<String> action=new ArrayList<String>();
	private ArrayList<String> person=new ArrayList<String>();
	private ArrayList<String> result=new ArrayList<String>();
	

	public void load(String path) throws IOException{
		BufferedReader br = new BufferedReader(new FileReader(path));
		String line;
		int i=0;
		while ((line = br.readLine()) != null) {
		   // process the line.
			//System.out.println(line);
			String[] splitline=line.split(",");
			colour.add(splitline[0]);
			size.add(splitline[1]);
			action.add(splitline[2]);
			person.add(splitline[3]);
			result.add(splitline[4]);
			
		}
		br.close();
	}
	public void print(){
		for(int i=0;i<colour.size();i++){
			System.out.println(colour.get(i)+","+size.get(i)+","+action.get(i)+","+person.get(i)+","+result.get(i));
		}
	}
}
