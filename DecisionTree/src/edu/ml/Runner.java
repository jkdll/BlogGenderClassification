package edu.ml;

import java.io.IOException;

import edu.ml.car.ReadDataset;
import edu.ml.loader.*;

public class Runner {
	public static void main(String[]args) throws IOException{
		DataSet dr = new DataSet("C:\\Users\\Jake\\Desktop\\ID3 Assignment\\DataSets\\Abalone\\abalone.data");
		dr.loadData();
		dr.printHeaders();
		dr.printData();
	}
}
