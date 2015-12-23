package mtest.mtesta;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.ThresholdUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.UserBasedRecommender;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws IOException, TasteException
    {
       DataModel model = new FileDataModel(new File("data/reviewconvert.csv"));
       UserSimilarity similarity = new PearsonCorrelationSimilarity(model);
       UserNeighborhood neighbohood = new ThresholdUserNeighborhood(0.9,similarity,model);
       System.out.println(neighbohood);
       UserBasedRecommender recommender = new GenericUserBasedRecommender(model,neighbohood,similarity);
       List<RecommendedItem> recommendations = recommender.recommend(14, 5);
       for (RecommendedItem recommendation:recommendations){
    	   System.out.println(recommendation);
    	   System.out.println(1);
       }
       System.out.println(2);
    }
}
