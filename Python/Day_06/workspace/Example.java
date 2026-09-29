public class Example {
    static void hello(){
        System.out.println("Hello");
    }

    public static void main(String[] args){
        Example.hello();

        Example ex1 = new Example();
        ex1.hello();
    }
}