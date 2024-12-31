from scipy.stats import f_oneway, ttest_ind
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


class ABanalysis:
    def __init__(self, data):
        self.data = data


    def test_risk_across_provinces(self):
        """
        Test if there are significant risk differences (Total Claims) across provinces.
        Null Hypothesis: There are no risk differences across provinces.
        """

        province_groups = [self.data[self.data['Province'] == p]['TotalClaims'] for p in self.data['Province'].unique()]
        result = f_oneway(*province_groups)
        return {
            "Test": "ANOVA",
            "Null Hypothesis": "No risk differences across provinces",
            "F-Statistic": result.statistic,
            "p-Value": result.pvalue,
            "Reject Null": result.pvalue < 0.05
        }
    

    def test_risk_difference_gender(self):
        """
        Test if there are significant risk differences (Total Claims) between genders.
        Null Hypothesis: There are no significant risk differences between women and men.
        """
        male_group = self.data[self.data['Gender'] == 'Male']['TotalClaims']
        female_group = self.data[self.data['Gender'] == 'Female']['TotalClaims']
        result = ttest_ind(male_group, female_group, equal_var=False)
        return {
            "Test": "T-Test",
            "Null Hypothesis": "No significant risk differences between women and men",
            "T-Statistic": result.statistic,
            "p-Value": result.pvalue,
            "Reject Null": result.pvalue < 0.05
        }
    
    def test_risk_between_PostalCode(self):
        """
        Test if there are significant risk differences (Total Claims) between PostalCode.
        Null Hypothesis: There are no risk differences between PostalCode.
        """
        zipcode_groups = [self.data[self.data['PostalCode'] == z]['TotalClaims'] for z in self.data['PostalCode'].unique()]
        result = f_oneway(*zipcode_groups)
        return {
            "Test": "ANOVA",
            "Null Hypothesis": "No risk differences between zip codes",
            "F-Statistic": result.statistic,
            "p-Value": result.pvalue,
            "Reject Null": result.pvalue < 0.05
        }
    