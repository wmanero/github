public class MainClass {

    public static boolean validarCPF(String cpf) {
        // Remove caracteres não numéricos
        cpf = cpf.replaceAll("\\D", "");

        // Verifica se o CPF tem 11 dígitos ou é uma sequência repetida
        if (cpf.length() != 11 || cpf.matches("(\\d)\\1{10}")) {
            return false;
        }

        try {
            // Calcula o primeiro dígito verificador
            int soma = 0;
            for (int i = 0; i < 9; i++) {
                soma += Character.getNumericValue(cpf.charAt(i)) * (10 - i);
            }
            int primeiroDigito = 11 - (soma % 11);
            if (primeiroDigito >= 10) primeiroDigito = 0;

            // Calcula o segundo dígito verificador
            soma = 0;
            for (int i = 0; i < 10; i++) {
                soma += Character.getNumericValue(cpf.charAt(i)) * (11 - i);
            }
            int segundoDigito = 11 - (soma % 11);
            if (segundoDigito >= 10) segundoDigito = 0;

            // Verifica se os dígitos calculados são iguais aos informados
            return primeiroDigito == Character.getNumericValue(cpf.charAt(9)) &&
                   segundoDigito == Character.getNumericValue(cpf.charAt(10));
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static void main(String[] args) {
        String cpf = "123.456.789-09"; // Substitua pelo CPF que deseja testar
        if (validarCPF(cpf)) {
            System.out.println("CPF válido.");
        } else {
            System.out.println("CPF inválido.");
        }
    }
}