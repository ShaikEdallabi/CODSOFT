import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Grade Calculator!");

        // Input marks for each subject
        System.out.print("Enter marks obtained in Subject 1 (out of 100): ");
        int subject1Marks = scanner.nextInt();

        System.out.print("Enter marks obtained in Subject 2 (out of 100): ");
        int subject2Marks = scanner.nextInt();

        System.out.print("Enter marks obtained in Subject 3 (out of 100): ");
        int subject3Marks = scanner.nextInt();

        // Calculate total marks
        int totalMarks = subject1Marks + subject2Marks + subject3Marks;

        // Calculate average percentage
        double averagePercentage = (double) totalMarks / 3;

        // Determine grade based on average percentage
        String grade;
        if (averagePercentage >= 90) {
            grade = "A";
        } else if (averagePercentage >= 80) {
            grade = "B";
        } else if (averagePercentage >= 70) {
            grade = "C";
        } else if (averagePercentage >= 60) {
            grade = "D";
        } else {
            grade = "F";
        }

        // Display results
        System.out.println("\nResults:");
        System.out.println("Total Marks: " + totalMarks);
        System.out.printf("Average Percentage: %.2f%%\n", averagePercentage);
        System.out.println("Grade: " + grade);

        scanner.close();
    }
}
