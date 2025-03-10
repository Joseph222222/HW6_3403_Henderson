#region imports
from Rankine import rankine

#endregion

#region main
def main():
    """
    This function instantiates 2 objects of the Rankine class with different attributes relating to different Rankine cycles
    1.  Saturated Vapor Turbine Inlet
    2.  Super Heated Vapor Inlet
    :return: nothing to return only output the print_summary method
    """
    t1 = rankine(p_high=8000,p_low=8,t_high=None,name='Saturated Vapor Turbine Inlet Cycle')
    t1.print_summary()
    #t_high for t2 should use griddata to find tsat at p_high and multiply by 1.7
    t2 = rankine(p_high=8000,p_low=8,t_high=295.06*1.7, name='Super Heated Vapor Turbine Inlet Cycle')
    t2.print_summary()

if __name__=="__main__":
    main()
#endregion