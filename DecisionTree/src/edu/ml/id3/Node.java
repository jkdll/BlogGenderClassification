package edu.ml.id3;

import java.util.ArrayList;

public class Node {
	private String attribute;
	private Node parent;
	private ArrayList<Node> children;
	
	public Node(String attribute,Node parent,ArrayList<Node> children){
		this.attribute=attribute;
		this.parent=parent;
		this.children=children;
	}

	public String getAttribute() {
		return attribute;
	}

	public void setAttribute(String attribute) {
		this.attribute = attribute;
	}

	public Node getParent() {
		return parent;
	}

	public void setParent(Node parent) {
		this.parent = parent;
	}

	public ArrayList<Node> getChildren() {
		return children;
	}

	public void setChildren(ArrayList<Node> children) {
		this.children = children;
	}
	
	
}
