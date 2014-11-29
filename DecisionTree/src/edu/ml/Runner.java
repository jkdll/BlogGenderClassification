package edu.ml;

import java.io.IOException;

import edu.ml.id3.DataSet;

public class Runner {
	public static void main(String[]args) throws IOException{
		DataSet ds = new DataSet();
		ds.readData("C:\\Users\\Jake\\Desktop\\ID3 Assignment\\DataSets\\Abalone\\abalone.data");
		ds.printHeaders();
	}
}
