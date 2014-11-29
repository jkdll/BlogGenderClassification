package edu.ml.loader;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import edu.ml.id3.Header;

public class DataSet {
	private ArrayList<Feature> headers;
	private Map<String, Double> nominal;
	private String path;
	private double [][] values;
	
	public DataSet(String p){
		this.headers = new ArrayList<Feature>();
		this.nominal = new HashMap<String,Double>();
		this.path = p;
	}
	
	public void loadData() throws IOException{
			FileInputStream fis = new FileInputStream(this.path);
			 
			//Construct BufferedReader from InputStreamReader
			BufferedReader br = new BufferedReader(new InputStreamReader(fis));
		 
			String line = null;
			int line_number = 0;
			int total_lines = 0;
			String [] temp;
			boolean collectedAllTypes = true;
			
			while ((line = br.readLine()) != null) {
				total_lines++;
			}
			System.out.println("Total Lines Read: " + total_lines + 1);
			br = new BufferedReader(new InputStreamReader(new FileInputStream(this.path)));
			
			while ((line = br.readLine()) != null) {
				if(line_number == 0){
					temp = line.split(",");
					for(int i = 0; i <= temp.length - 1; i++){
						headers.add(new Feature(temp[i]));
					}
					values = new double[headers.size()][total_lines + 1];
					line_number++;
				} else {
					temp = line.split(",");
					for(int i = 0; i <= temp.length - 1; i++){
						if(isDouble(temp[i])){
							values[i][line_number] = Double.parseDouble(temp[i]);
							headers.get(i).setFeatureType(DataType.LINEAR);
						} else {
							values[i][line_number] = addNominal(temp[i]);
							headers.get(i).setFeatureType(DataType.NOMINAL);
						}
					}
				}
			}
			
			br.close();	
	}
	
	public void printHeaders(){
		for(int i = 0; i <= headers.size() - 1; i++){
			System.out.println(headers.get(i).getFeatureName() + " " + headers.get(i).getFeatureType().toString());
		} 
	}
	
	private double addNominal(String s){
		if(nominal.isEmpty() == true){
			nominal.put(s, 1.0);
			return nominal.get(s);
		} else if(nominal.containsKey(s)) {
			return nominal.get(s);
		}
			nominal.put(s, Collections.max(nominal.values()) + 1.0);
			return nominal.get(s);
	}

	private boolean isDouble(String s){
		try
		{
		  Double.parseDouble(s);
		  return true &&  s.contains(".");
		}
		catch(NumberFormatException e)
		{
		  return false;
		}
	}

	public void printCats(){
		for (Map.Entry<String, Double> entry : nominal.entrySet()) {
	        String key = entry.getKey().toString();
	        Double value = entry.getValue();
	        System.out.println("key, " + key + " value " + value );
	    }
	}
	public void printData(){
		for(int i = 0; i <= values.length - 1; i++){
			System.out.print( values[i][0] + ",");
		}
	}
}
