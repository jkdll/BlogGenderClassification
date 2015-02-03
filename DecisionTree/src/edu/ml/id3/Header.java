package edu.ml.id3;

public class Header {
	public Header(String n, boolean r){
		this.name = n;
		this.isContinuous = r;
	}
	private String name;
	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}
	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
	/**
	 * @return the isContinuous
	 */
	public boolean isContinuous() {
		return isContinuous;
	}
	/**
	 * @param isContinuous the isContinuous to set
	 */
	public void setContinuous(boolean isContinuous) {
		this.isContinuous = isContinuous;
	}
	private boolean isContinuous;

}
