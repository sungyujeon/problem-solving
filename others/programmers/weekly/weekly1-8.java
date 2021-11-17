package others.programmers.weekly;
// 프로그래머스 위클리챌린지
// 최소직사각형

class Solution {
    public static void main(String[] args) {
        int[][] sizes = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
        System.out.println(solution(sizes));
    }

    public static int solution(int[][] sizes) {
        int answer = 0;
        int left_max = 0;
        int right_max = 0;

        for (int i = 0; i < sizes.length; i++) {
            int left = sizes[i][0];
            int right = sizes[i][1];
            if (sizes[i][0] < sizes[i][1]) {
                left = sizes[i][1];
                right = sizes[i][0];
            }

            if (left > left_max) {
                left_max = left;
            }

            if (right > right_max) {
                right_max = right;
            }
        }
        answer = left_max * right_max;
        
        return answer;
    }
}