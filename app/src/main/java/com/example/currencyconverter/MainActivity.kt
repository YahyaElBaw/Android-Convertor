package com.example.currencyconverter

import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.currencyconverter.databinding.ActivityMainBinding

/**
 * Activité principale de l'application Currency Converter.
 * Développée avec View Binding, TableLayout personnalisé et gestion rigoureuse des règles de saisie.
 */
class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // 1. Initialisation des Spinners avec ArrayAdapter
        configurerSpinners()

        // 2. Configuration des boutons du clavier numérique personnalisé
        configurerClavier()

        // 3. Bouton Convertir
        binding.btnConvertir.setOnClickListener {
            lancerConversion()
        }

        // 4. Bouton Inverser les devises
        binding.btnInverser.setOnClickListener {
            inverserDevises()
        }
    }

    /**
     * Remplit les Spinners à partir de la ressource R.array.devises
     * et positionne par défaut USD en source et EUR en cible.
     */
    private fun configurerSpinners() {
        val adapter = ArrayAdapter.createFromResource(
            this,
            R.array.devises,
            android.R.layout.simple_spinner_item
        )
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

        binding.spDeviseSource.adapter = adapter
        binding.spDeviseCible.adapter = adapter

        // Sélection par défaut : USD en source (index 0) et EUR en cible (index 1)
        val devises = resources.getStringArray(R.array.devises)
        val indexUsd = devises.indexOf("USD")
        val indexEur = devises.indexOf("EUR")

        if (indexUsd >= 0) binding.spDeviseSource.setSelection(indexUsd)
        if (indexEur >= 0) binding.spDeviseCible.setSelection(indexEur)

        // Bonus : Recalcul automatique si le résultat est déjà affiché
        val listener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
                if (binding.tvResultat.text.isNotEmpty()) {
                    lancerConversion(silentToast = true)
                }
            }
            override fun onNothingSelected(parent: AdapterView<*>?) {}
        }

        binding.spDeviseSource.onItemSelectedListener = listener
        binding.spDeviseCible.onItemSelectedListener = listener
    }

    /**
     * Associe chaque touche du TableLayout à sa fonction.
     */
    private fun configurerClavier() {
        val touchesChiffres = mapOf(
            binding.btn0 to "0",
            binding.btn1 to "1",
            binding.btn2 to "2",
            binding.btn3 to "3",
            binding.btn4 to "4",
            binding.btn5 to "5",
            binding.btn6 to "6",
            binding.btn7 to "7",
            binding.btn8 to "8",
            binding.btn9 to "9",
            binding.btnPoint to "."
        )

        for ((bouton, caractere) in touchesChiffres) {
            bouton.setOnClickListener {
                ajouterCaractere(caractere)
            }
        }

        binding.btnC.setOnClickListener {
            // La touche « C » remet le montant à « 0 » et vide le résultat
            binding.tvMontant.text = getString(R.string.valeur_initiale)
            binding.tvResultat.text = ""
        }
    }

    /**
     * Ajoute un caractère au montant en respectant les contraintes :
     * - Limite à 10 caractères
     * - Remplacement du 0 initial
     * - Un seul point décimal autorisé
     */
    private fun ajouterCaractere(c: String) {
        val texteActuel = binding.tvMontant.text.toString()

        // Contrainte 1 : maximum 10 caractères
        if (texteActuel.length >= 10) {
            return
        }

        // Contrainte 2 : un seul point décimal
        if (c == "." && texteActuel.contains(".")) {
            return
        }

        val nouveauTexte = when {
            // Si le montant actuel est "0" et qu'on tape un chiffre, on le remplace
            texteActuel == "0" && c != "." -> c
            // Si le montant actuel est "0" et qu'on tape ".", cela donne "0."
            texteActuel == "0" && c == "." -> "0."
            else -> texteActuel + c
        }

        binding.tvMontant.text = nouveauTexte
    }

    /**
     * Effectue la conversion et affiche le résultat formatté à 2 décimales.
     */
    private fun lancerConversion(silentToast: Boolean = false) {
        val texteMontant = binding.tvMontant.text.toString()
        val montant = texteMontant.toDoubleOrNull() ?: 0.0

        if (montant == 0.0) {
            if (!silentToast) {
                Toast.makeText(this, R.string.erreur_montant_nul, Toast.LENGTH_SHORT).show()
            }
            return
        }

        val source = binding.spDeviseSource.selectedItem?.toString() ?: "USD"
        val cible = binding.spDeviseCible.selectedItem?.toString() ?: "EUR"

        val resultat = CurrencyConverter.convertir(montant, source, cible)
        binding.tvResultat.text = CurrencyConverter.formater(resultat)
    }

    /**
     * Échange les sélections des deux Spinners et relance la conversion si un résultat est présent.
     */
    private fun inverserDevises() {
        val posSource = binding.spDeviseSource.selectedItemPosition
        val posCible = binding.spDeviseCible.selectedItemPosition

        binding.spDeviseSource.setSelection(posCible)
        binding.spDeviseCible.setSelection(posSource)

        if (binding.tvResultat.text.isNotEmpty()) {
            lancerConversion(silentToast = true)
        }
    }
}
