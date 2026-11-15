def estimate(input_tokens,output_tokens,input_rate,output_rate):
    return (input_tokens*input_rate+output_tokens*output_rate)/1_000_000
