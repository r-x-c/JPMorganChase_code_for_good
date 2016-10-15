import java.awt.PageAttributes.MediaType;
import java.sql.*;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import org.json.*;
import java.util.ArrayList;

import javax.ws.rs.*;

@Path("/choices/")
public class ResCalls {
	Connection conn = null;
	Statement stmt = null;

	public static void main(String[] args) {
		ResCalls r = new ResCalls();
		r.getQuestion();
	}

	private static void printMap(Map<String, Integer> mp) {
		Iterator it = mp.entrySet().iterator();
		while (it.hasNext()) {
			HashMap.Entry pair = (HashMap.Entry) it.next();
			System.out.println(pair.getKey() + " = " + pair.getValue());
			it.remove(); // avoids a ConcurrentModificationException
		}
	}


	// @GET
	// @Path("/getLocations/")
	// @Produces(MediaType.APPLICATION_JSON)
	public void getGeneral(String name) {
		Map<String, Integer> hash = new HashMap<String, Integer>();

		String sqL = "SELECT " + name + " FROM user_t";
		try {
			ResultSet rs = getConnection().executeQuery(sqL);

			while (rs.next()) {
				// Retrieve by column name
				String ans = rs.getString(name);
				if (hash.containsKey(ans)) {
					int num = hash.get(ans);
					hash.put(ans, num + 1);
				} else {
					hash.put(ans, 1);
				}
			}

			JSONObject returnedJSON = new JSONObject(hash);
			// printMap(hash);
			System.out.println(returnedJSON);
			closeConnection();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	public void getLocations() {
		getGeneral("location");
	}

	public void getAge() {
		Map<String, Integer> hash = new HashMap<String, Integer>();

		String sqL = "SELECT age FROM user_t";
		try {
			ResultSet rs = getConnection().executeQuery(sqL);

			while (rs.next()) {
				// Retrieve by column name
				String ans = rs.getString("age");
				if (hash.containsKey(ans)) {
					int num = hash.get(ans);
					hash.put(ans, num + 1);
				} else {
					hash.put(ans, 1);
				}
			}
			printMap(hash);
			closeConnection();
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}

	public void getGender() {
		getGeneral("gender");
	}

	public void getRace() {
		getGeneral("race");
	}

	public void getQuestion() {
		Map<String, ArrayList<String>> qhash = new HashMap<String, ArrayList<String>>();

		String sqQ = "SELECT question_id, q_text FROM question_t";
		try {
			ResultSet rs = getConnection().executeQuery(sqQ);

			while (rs.next()) {
				// Retrieve by column name
				int id = rs.getInt("question_id");
				String q_str = rs.getString("q_text");
				String ans = "SELECT * FROM answer_t WHERE question_id = " + id;
				ResultSet rsAns = getConnection().executeQuery(ans);
				ArrayList<String> ansList = new ArrayList<String>();
				while (rsAns.next()) {
					ansList.add(rsAns.getString("answer"));
				}
				qhash.put(q_str, ansList);
			}
			JSONObject returnedJSON = new JSONObject(qhash);
			System.out.println(returnedJSON);
			closeConnection();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	private Statement getConnection() {

		try {
			Class.forName("com.mysql.cj.jdbc.Driver").newInstance();
			conn = DriverManager.getConnection("jdbc:mysql://52.87.182.66:3306/choices", "root", "root");
			stmt = conn.createStatement();
			return stmt;
		} catch (SQLException se) {
			// Handle errors for JDBC
			se.printStackTrace();
			return null;
		} catch (Exception e) {
			// Handle errors for Class.forName
			e.printStackTrace();
			return null;
		}
		// finally block used to close resources
		// end finally try
	}

	private void closeConnection() {
		try {
			if (stmt != null)
				stmt.close();
		} catch (SQLException se2) {
		} // nothing we can do
		try {
			if (conn != null)
				conn.close();
		} catch (SQLException se) {
			se.printStackTrace();
		}
	}
}
