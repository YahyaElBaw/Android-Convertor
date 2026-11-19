package com.example.currencyconverter

import java.util.Locale

/**
 * Logique métier de conversion de devises avec passage par l'Euro comme devise pivot.
 */
object CurrencyConverter {

    /**
     * Taux de change fixes par rapport à 1 EUR imposés par le sujet du TP.
     */
    val taux: Map<String, Double> = mapOf(
        "EUR" to 1.00,
        "USD" to 1.17,
        "TND" to 3.40,
        "GBP" to 0.87,
        "JPY" to 172.50,
        "CAD" to 1.62
    )

    /**
     * Convertit un montant d'une devise source vers une devise cible.
     * Formule :
     *   montant en EUR = montant / taux(source)
     *   résultat = montant en EUR * taux(cible)
     */
    fun convertir(montant: Double, source: String, cible: String): Double {
        if (source == cible) {
            return montant
        }
        val tauxSource = taux[source] ?: throw IllegalArgumentException("Devise source inconnue : $source")
        val tauxCible = taux[cible] ?: throw IllegalArgumentException("Devise cible inconnue : $cible")

        val montantEnEur = montant / tauxSource
        return montantEnEur * tauxCible
    }

    /**
     * Formate le résultat avec exactement deux chiffres après la virgule.
     */
    fun formater(valeur: Double): String {
        return String.format(Locale.US, "%.2f", valeur)
    }
}
