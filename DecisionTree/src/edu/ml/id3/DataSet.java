package edu.ml.id3;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class DataSet {
	private String path;
	private ArrayList<Header> headers;
	private Map<String, Double> nominal; 
	private Double[][] values;
	
	public DataSet(){
		this.headers = new ArrayList<Header>();
		this.nominal = new HashMap<String,Double>();
	}
	
	public void readData(String path) throws IOException{
		FileInputStream fis = new FileInputStream(path);
		 
		//Construct BufferedReader from InputStreamReader
		BufferedReader br = new BufferedReader(new InputStreamReader(fis));
	 
		String line = null;
		String [] temp;
		boolean isFirstLine = true;
		int noLines = 0;
		
		while ((line = br.readLine()) != null){
			noLines++;
		}
		
		br.close();
		
		br = new BufferedReader(new InputStreamReader(fis));
		
		while ((line = br.readLine()) != null) {
			// If This is the first line, then read the headers...
			if(isFirstLine == true){
				temp = line.split(",");
				for(int i = 0; i <= temp.length - 1; i++){
					headers.add(new Header(temp[i],false));
				}
				isFirstLine = false;
				noLines = noLines - 1;
				values = new Double[noLines][headers.size()];
			} else { 
				temp = line.split(",");
				for(int i = 0; i<= temp.length - 1; i++){
					if(isDouble(temp[i])){
						
					}
				}
			}
		}
	 
		br.close();
	}
	
	boolean isDouble(String str) {
        try {
            Double.parseDouble(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
	
	boolean isInteger(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
	
	public void printHeaders(){
		for (Header h : headers) {
		    System.out.println(h.getName() + " - " + h.isContinuous());
		}
	}
	
	private void addNominal(String label){
		if(nominal.get(label) == null){ // Check if nominal value exists already.
			if(nominal.isEmpty()){
				// If this is the first Nominal Value, we start at 1.0
				nominal.put(label, 1.0);
			} else {
				// Otherwise Create a new Nominal value with a +1 over the max.
				nominal.put(label, Collections.max(nominal.values()) + 1.0);
			}
		}
	}
}
