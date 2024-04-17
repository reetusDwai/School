int hashISBN(int isbn){
    int start = 12345;
    int partA = isbn % 1000;
    int partB = start * partA - isbn;
    int partC = partB % 100000;
    int partD = partC + start;
    return partD % 100000;
}
