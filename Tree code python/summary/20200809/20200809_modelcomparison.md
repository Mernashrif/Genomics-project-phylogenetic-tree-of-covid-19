# initial `phydms` analysis with SARS-Cov-2 RBD DMS preferences

August 9, 2020

`pandoc 20200809_modelcomparison.md --pdf-engine=xelatex -o 20200809_modelcomparison.pdf --toc -V geometry:margin=1in --variable urlcolor=magenta`

## goal

Evaluate how well the expression and binding data from the RBD DMS explain the natural sequence evolution of SARS RBDs.

## data

### sequences

The alignment has a total of 23 sequences from Bat-SARS-related-CoV(non Asian), SARS-CoV-1 Clade, and SARS-CoV-2 Clade.

### preferences

The RBD DMS experiment had two experimental conditions: expression and binding.
I calculated preferences for each condition using the code Jesse made to make logoplots in the paper, specifically calculating probability.
You can find more information in [Jesse's notebook](https://github.com/jbloomlab/SARS-CoV-2-RBD_DMS/blob/master/logoplots_of_muteffects.ipynb).

## results

Here is the model comparison file:

| Model                          | deltaAIC | LogLikelihood | nParams | ParamValues                                              |
|--------------------------------|----------|---------------|---------|----------------------------------------------------------|
| ExpCM_expr_gammaomega          | 0.00     | -2956.51      | 7       | alpha_omega=0.40, beta=1.54, beta_omega=0.86, kappa=2.13 |
| ExpCM_expr                     | 167.06   | -3041.04      | 6       | beta=1.49, kappa=1.71, omega=0.26                        |
| ExpCM_bind_gammaomega          | 248.82   | -3080.92      | 7       | alpha_omega=0.35, beta=1.68, beta_omega=0.97, kappa=2.01 |
| ExpCM_bind                     | 429.76   | -3172.39      | 6       | beta=1.95, kappa=1.73, omega=0.22                        |
| YNGKP_M5                       | 834.80   | -3368.91      | 12      | alpha_omega=0.30, beta_omega=2.03, kappa=1.74            |
| averaged_ExpCM_expr_gammaomega | 856.18   | -3384.60      | 7       | alpha_omega=0.30, beta=1.11, beta_omega=1.28, kappa=1.90 |
| averaged_ExpCM_bind_gammaomega | 866.48   | -3389.75      | 7       | alpha_omega=0.30, beta=0.00, beta_omega=1.33, kappa=1.92 |
| averaged_ExpCM_expr            | 1104.86  | -3509.94      | 6       | beta=1.55, kappa=1.72, omega=0.11                        |
| averaged_ExpCM_bind            | 1124.80  | -3519.91      | 6       | beta=0.00, kappa=1.76, omega=0.11                        |
| YNGKP_M0                       | 1133.36  | -3519.19      | 11      | kappa=1.57, omega=0.06                                   |
