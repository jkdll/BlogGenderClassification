package edu.ml.car;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class ReadDataset {
	public void run() {

		String csvFile = "/Users/andre_000/machinelearning/DecisionTree/car/car.data";
		BufferedReader br = null;
		String line = "";
		String cvsSplitBy = ",";
		
		/*ArrayList<String> buying=new ArrayList<String>();
		ArrayList<String> maintenance=new ArrayList<String>();
		ArrayList<String> doors=new ArrayList<String>();
		ArrayList<String> persons=new ArrayList<String>();
		ArrayList<String> lug_boot=new ArrayList<String>();
		ArrayList<String> safety=new ArrayList<String>();
		ArrayList<String> value=new ArrayList<String>();*/
		
		ArrayList<String[]> dataset = new ArrayList<String[]>();

		try {

			br = new BufferedReader(new FileReader(csvFile));
			while ((line = br.readLine()) != null) {

				// use comma as separator
				String[] car = line.split(cvsSplitBy);
				
				dataset.add(car);
//				
//				System.out.println(car[0] + " " + car[1] + " " + car[2] + " "
//						+ car[3] + " " + car[4] + " " + car[5] + " " + car[6]);

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
		printDataSet(dataset);
	}
	
	private void printDataSet(ArrayList<String[]> dataset){
		for (int i=0;i<dataset.size();i++){
			for (int j=0;j<7;j++){
				System.out.println(dataset.get(i)[j]);
			}
			System.out.println("------------------"+i);
		}
	}

}
