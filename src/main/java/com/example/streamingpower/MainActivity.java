package com.example.streamingpower;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import android.content.res.Configuration;

public class MainActivity extends AppCompatActivity {
    // on below line creating a variable for web view.
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // on below line initializing web view with id.
        webView = findViewById(R.id.webView);

        // on below line setting web view client.
        webView.setWebViewClient(new WebClient());

        // on below line setting web chrome client for web view.
        webView.setWebChromeClient(new WebChromeClient());

        // on below line getting web settings.
        WebSettings webSettings = webView.getSettings();

        // on below line setting java script enabled to true.
        webSettings.setJavaScriptEnabled(true);

        // on below line setting file access to true.
        webSettings.setAllowFileAccess(true);

        // on below line setting url for the web page which we have to load in our web view.
        webView.loadUrl("https://lizziewizzie.site/streamingpower");
    }

    // on below line creating a class for web chrome client.
    class WebChromeClient extends android.webkit.WebChromeClient {
        // on below line creating variables.
        private View customView;
        private android.webkit.WebChromeClient.CustomViewCallback customViewCallback;
        private int originalOrientation;
        private int originalSystemVisibility;

        WebChromeClient() {
        }

        @Nullable
        @Override
        public Bitmap getDefaultVideoPoster() {

            // on below line returning our resource from bitmap factory.
            if (customView == null) {
                return null;
            }
            return BitmapFactory.decodeResource(getApplicationContext().getResources(), 2130837573);
        }

        @Override
        public void onHideCustomView() {

            // on below line removing our custom view and setting it to null.
            ((FrameLayout) getWindow().getDecorView()).removeView(customView);
            this.customView = null;

            // on below line setting system ui visibility to original one and setting orientation for it.
            getWindow().getDecorView().setSystemUiVisibility(this.originalSystemVisibility);
            setRequestedOrientation(this.originalOrientation);

            // on below line setting custom view call back to null.
            this.customViewCallback.onCustomViewHidden();
            this.customViewCallback = null;
        }

        @Override
        public void onShowCustomView(View view, CustomViewCallback callback) {
            if (this.customView != null) {
                onHideCustomView();
                return;
            }


            // on below line initializing all variables.
            this.customView = view;
            this.originalSystemVisibility = getWindow().getDecorView().getSystemUiVisibility();
            this.originalOrientation = getRequestedOrientation();
            this.customViewCallback = callback;
            ((FrameLayout) getWindow().getDecorView()).addView(this.customView, new FrameLayout.LayoutParams(-1, -1));
            getWindow().getDecorView().setSystemUiVisibility(3846);
        }
    }
    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);

        // Vérifie si l'orientation a changé
        if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE) {
            // Gère l'orientation paysage ici, par exemple ne fais rien ou ajuste l'UI si nécessaire
        } else if (newConfig.orientation == Configuration.ORIENTATION_PORTRAIT) {
            // Gère l'orientation portrait ici, par exemple ne fais rien ou ajuste l'UI si nécessaire
        }
    }

    // on below line creating a class for Web Client.
    class WebClient extends WebViewClient {
        @Override
        public void onPageStarted(WebView view, String url, Bitmap favicon) {
            super.onPageStarted(view, url, favicon);
        }

        @Override
        public void onPageFinished(WebView view, String url) {
            super.onPageFinished(view, url);
        }
    }
}