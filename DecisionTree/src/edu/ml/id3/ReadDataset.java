package edu.ml.id3;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ReadDataset {
	public void run() {
		 
		String csvFile = "/Users/andre_000/machinelearning/DecisionTree/car/car.data";
		BufferedReader br = null;
		String line = "";
		String cvsSplitBy = ",";
	 
		try {
	 
			br = new BufferedReader(new FileReader(csvFile));
			while ((line = br.readLine()) != null) {
	 
			        // use comma as separator
				String[] car = line.split(cvsSplitBy);
	 
				System.out.println(car[0] +" "+car[1]+" "+car[2]+" "+car[3]+" "+car[4]+" "+car[5]+" "+car[6]);
	 
			}
	 
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	 
		System.out.println("Done");
	  }
	 
	}

