package edu.ml.loader;

public class Feature {
	public Feature(){
		
	}
	public Feature(String n){
		this.featureName = n;
	}
	public Feature(String n, DataType t){
		this.featureName = n;
		this.featureType = t;
	}
	private String featureName;
	/**
	 * @return the featureName
	 */
	public String getFeatureName() {
		return featureName;
	}
	/**
	 * @param featureName the featureName to set
	 */
	public void setFeatureName(String featureName) {
		this.featureName = featureName;
	}
	/**
	 * @return the featureType
	 */
	public DataType getFeatureType() {
		return featureType;
	}
	/**
	 * @param featureType the featureType to set
	 */
	public void setFeatureType(DataType featureType) {
		this.featureType = featureType;
	}
	private DataType featureType;
	
}
