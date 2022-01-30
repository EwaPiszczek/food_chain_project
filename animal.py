class Animal:
    """
    A class which is representing animal

    Attributes
    ----------
    name : str
        The name of the animal in the food chain
    species: str
        The species of the animal in the food chain (Producers and Decomposers, Primary Consumers, Tertiary Consumers)
    level: int
        The level in the food chain

    Methods
    -------
    __init__(name, specie, level, consumers)
        the method responsible for creation of Animal object

    getName()
        the method responsible for returning the name of the animal as str 
    
    getSpecie()
        the method responsible for returning the specie of the animal 

    getLevel()
        the method responsible for returning the level of the animal in the food chain

    getConsumers
        the method responsible for returning all consumers of this animal (if animal is at the top of the hierarchy, method returns "None")

    """

    def __init__(self, name, specie, level, consumers):
        """
        Parameters
        ----------
        name : str
            The name of the animal in the food chain
        specie : str
            The specie of the animal in the food chain (Producers and Decomposers, Primary Consumers, Tertiary Consumers)
        level : int
            The level of the animal in the food chain
        consumers : array of str
            All consumers of this animal
        
        """
        self.name = name
        self.specie = specie
        self.level = level
        self.consumers = consumers
        if "None" not in self.consumers:
            self.consumers = self.consumers.split("|")
        else:
            self.consumers = ["None"]

    def getName(self):
        """
        Parameters
        ----------
        None

        Return
        ----------
        str :
            The name of the animal as str 
        
        """ 
        return self.name

    def getSpecie(self):
        """
        Parameters
        ----------
        None

        Return
        ----------
        str :
            The specie of the animal 
        
        """ 
        return self.specie

    def getLevel(self):
        """
        Parameters
        ----------
        None

        Return
        ----------
        str :
            The level of the animal in the food chain
        
        """ 
        return self.level
    
    def getConsumers(self):
        """
        Parameters
        ----------
        None

        Return
        ----------
        array of str : 
            All consumers of this animal (if animal is at the top of the hierarchy, method returns "None")
        
        """ 
        if "None" in self.consumers:
            return ["None"]
        else:
            return self.consumers