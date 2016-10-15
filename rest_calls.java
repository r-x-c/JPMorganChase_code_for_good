import java.sql.*;
import javax.ws.rs.*;

@Path("/choices/")
public class ResCalls {
	Connection conn = null;
	Statement stmt = null;

	public static void main(String[] args){
		ResCalls r = new ResCalls();
		r.getLocations();
	}
	
//	@GET
//	@Path("/getLocations/")
//	@Produces("application/json")
	public String getLocations() {
		String sqL = "SELECT location FROM user_t";
		try {
			ResultSet rs = getConnection().executeQuery(sqL);

			while (rs.next()) {
				// Retrieve by column name
				String location = rs.getString("location");
				// Display values
				System.out.print("Location: " + location);
			}
			closeConnection();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return null;
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
